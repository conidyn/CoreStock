import { API_BASE_URL } from "@/config/api";

export type StockItemProduct = {
  id: number;
  name: string;
  sku: string;
};

export type StockItemLocation = {
  id: number;
  name: string;
  type: string;
};

export type StockItem = {
  id: number;
  quantity: number;
  product: StockItemProduct;
  location: StockItemLocation;
};

export async function getStockItems(): Promise<StockItem[]> {
  const response = await fetch(`${API_BASE_URL}/api/stock-items`);

  if (!response.ok) {
    throw new Error("Failed to fetch stock items");
  }

  return response.json();
}