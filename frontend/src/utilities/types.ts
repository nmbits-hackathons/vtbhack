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

interface TransactionSummary {
  amount: string;
  transactionType: 'marketplace' | 'events' | 'thanks'| 'nft';
}

interface TransactionsData {
  date: Date,
  transactions: TransactionSummary[]
}

interface MarketplaceItem {
  image: string;
  price: number;
  title: string;
  size?: 'sm' | 'md' | 'big';
}

interface NFTItem {
  image: string;
  collection: string;
  title: string;
  size?: 'sm' | 'md' | 'big';
}

export {
  User,
  Wallet,
  NewsRecord,
  TransactionSummary,
  TransactionsData,
  MarketplaceItem,
  NFTItem
}