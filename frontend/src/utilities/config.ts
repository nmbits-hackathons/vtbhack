import { useCookies } from "vue3-cookies";
import axios from "axios";

const { cookies } = useCookies();

const emailRegExp =
  /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;


const defaultWalletUrl = 'https://hackathon.lsp.team/hk'
const defaultBackUrl = 'http://45.67.228.220:7171/'

const apiWallet = `${process.env.VUE_APP_WALLET_SERVER || defaultWalletUrl}/`
const apiBack = `${process.env.VUE_APP_BACK_SERVER || defaultBackUrl}/`

const instance_wallet = axios.create({
  withCredentials: false,
  baseURL: apiWallet
})

const instance_user = axios.create({
  withCredentials: false,
  baseURL: apiBack
})

export {
  cookies,
  emailRegExp,
  instance_wallet,
  instance_user
}