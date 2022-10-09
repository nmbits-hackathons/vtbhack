import { User } from "@/utilities/types";

const initialState = () => {
  return {
    id: '6',
    name: "Александр Грин"
  } as User
}

const userModuleState = initialState

export { userModuleState, initialState }