import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "export",  // هذا السطر يضمن بناء مجلد 'out' يحتوي على ملفات HTML/CSS/JS فقط
  images: {
    unoptimized: true, // هذا هو الحل لمشكلة اللوجو: يمنع Next.js من محاولة معالجة الصور ويعرضها كما هي
  },
};

export default nextConfig;
