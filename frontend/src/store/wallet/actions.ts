import { ActionTree } from "vuex";
import { Wallet } from "@/utilities/types";
import { instance_wallet } from "@/utilities/config";

const walletModuleActions = <ActionTree<Wallet, null>>{
  async init(context) {
    const { data } = await instance_wallet.post('/v1/wallets/new')

    context.commit('setState', {
      key: 'publicKey',
      value: data.publicKey
    })
    context.commit('setState', {
      key: 'privateKey',
      value: data.privateKey
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