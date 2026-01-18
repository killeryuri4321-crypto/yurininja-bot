
console.log("🚀 Bot Yurininja iniciado");

// Dias permitidos: sexta (5), sábado (6), domingo (0)
const dia = new Date().getDay();

if (![0, 5, 6].includes(dia)) {
  console.log("⛔ Hoje não é dia de sinais. Bot desligado.");
  process.exit();
}

console.log("✅ Hoje é dia de sinais! Bot ativo.");