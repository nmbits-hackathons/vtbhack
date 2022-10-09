import { ActionTree } from "vuex";
import { Wallet } from "@/utilities/types";
import { instance_wallet } from "@/utilities/config";
import store from "..";

const walletModuleActions = <ActionTree<Wallet, null>>{
  async init(context) {
    const { data: balance } = await instance_wallet.get(`/v1/wallets/${
      store.state!['user']['public_key']
    }/balance`)
    const { data: history } = await instance_wallet.post(`/v1/wallets/${store.state!['user']['public_key']}/history`, {
      "page": 100,
      "offset": 20,
      "sort": "asc"
    })

    context.commit('setState', {
      key: 'matic',
      value: balance.maticAmount
    })
    context.commit('setState', {
      key: 'coins',
      value: balance.coinsAmount
    })

    context.commit('setState', {
      key: 'history',
      value: history.history
    })

  },
  transferMatic({state}, {toPublicKey, amount}) {
    return new Promise((resolve, reject) => {
      instance_wallet.post('/v1/wallets/new', {
        "fromPrivateKey": state.privateKey,
        "toPublicKey": toPublicKey,
        "amount": amount
      })
      .then((res) => {
        resolve(res.data.transactionHash)
      })
      .catch(e => reject(e))
    })
  }

};

export { walletModuleActions };