import { Wallet } from "@/utilities/types";

const initialState = () => {
  return {
    wallet: ''
  } as Wallet
}

const walletModuleState = initialState

export { walletModuleState, initialState }