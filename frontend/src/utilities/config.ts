import { useCookies } from "vue3-cookies";
import axios from "axios";

const { cookies } = useCookies();

const emailRegExp =
  /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;


const defaultWalletUrl = 'https://hackathon.lsp.team/hk'
const defaultBackUrl = ''

const apiWallet = `${process.env.VUE_APP_WALLET_SERVER || defaultWalletUrl}/`

const instance_wallet = axios.create({
  withCredentials: false,
  baseURL: apiWallet
})

export {
  cookies,
  emailRegExp,
  instance_wallet
}