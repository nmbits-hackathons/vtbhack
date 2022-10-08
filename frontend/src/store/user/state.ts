import { User } from "@/utilities/types";

const initialState = () => {
  return {
    id: '1',
    first_name: "Александр",
    last_name: "Грин"
  } as User
}

const userModuleState = initialState

export { userModuleState, initialState }