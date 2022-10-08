interface User {
  id: string;
  email?: string;
  first_name?: string;
  last_name?: string;
  role?: 'user' | 'moderator' | 'admin';
}

interface Wallet {
  publicKey: string;
  privateKey: string;
  matic?: number;
  coins?: number;
}

interface NewsRecord {
  type: string;
  title?: string;
  description?: string;
  award?: string;
  date?: Date;
}

export {
  User,
  Wallet,
  NewsRecord
}