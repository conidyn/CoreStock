import { API_BASE_URL } from "@/config/api";

export type Product = {
  id: number;
  name: string;
  sku: string;
  category: string;
  unit: string;
  min_stock_threshold: number;
};

export async function getProducts(): Promise<Product[]> {
  const response = await fetch(`${API_BASE_URL}/api/products`);

  if (!response.ok) {
    throw new Error("Failed to fetch products");
  }

  return response.json();
}