import { User } from "@/utilities/types";

const initialState = () => {
  return {
    id: ''
  } as User
}

const userModuleState = initialState

export { userModuleState, initialState }