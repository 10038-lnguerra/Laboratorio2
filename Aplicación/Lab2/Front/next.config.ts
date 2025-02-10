import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  env: {
    BACKEND_URL: "http://127.0.0.1:8000", // URL del backend Django
  },
};

export default nextConfig;
