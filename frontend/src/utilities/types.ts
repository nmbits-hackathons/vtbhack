interface User {
  id: string;
  email?: string;
  first_name?: string;
  last_name?: string;
  role?: 'user' | 'moderator' | 'admin';
}

interface Wallet {
  wallet: string;
  matic?: number;
  coins?: number;
}

export {
  User,
  Wallet
}