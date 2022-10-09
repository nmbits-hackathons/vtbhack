import { Wallet } from "@/utilities/types";

const initialState = () => {
  return {
    matic: 1200.83,
    coins: 345.35
  } as Wallet
}

const walletModuleState = initialState

export { walletModuleState, initialState }