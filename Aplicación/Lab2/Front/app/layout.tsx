export const metadata = {
  title: "Generador de Cuentos",
  description: "Crea cuentos con IA y conviértelos en voz.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <body className="bg-gray-50 min-h-screen">{children}</body>
    </html>
  );
}
