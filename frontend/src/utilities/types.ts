interface User {
  id: string;
  email?: string;
  name?: string;
  admin_role?: boolean,
  permission_nft_release?: boolean,
  permission_transfer_treasury?: boolean,
  permission_moderate_marketplace?: boolean,
  permission_events?: boolean,
  publicKey: string,
  privateKey: string
}

interface Event {
  title: string,
  description?: string,
  date_publication?: Date,
  date_event?: Date,
  creator?: number,
  type: string,
  reward?: number
}

interface Utilities {
  events?: Event[]
}

interface Wallet {
  publicKey: string;
  privateKey: string;
  matic?: number;
  coins?: number;
  history?: any[];
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
  TransactionSummary,
  TransactionsData,
  MarketplaceItem,
  NFTItem,
  Utilities,
  Event
}