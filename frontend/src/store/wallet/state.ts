import { Wallet } from "@/utilities/types";

const initialState = () => {
  return {
    publicKey: '',
    privateKey: ''
  } as Wallet
}

const walletModuleState = initialState

export { walletModuleState, initialState }