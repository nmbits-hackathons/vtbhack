import { User } from "@/utilities/types";

const initialState = () => {
  return {
    id: '6',
  } as User
}

const userModuleState = initialState

export { userModuleState, initialState }