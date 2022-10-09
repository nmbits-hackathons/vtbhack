import { Wallet } from "@/utilities/types";

const initialState = () => {
  return {
    matic: 0,
    coins: 0
  } as Wallet
}

const walletModuleState = initialState

export { walletModuleState, initialState }