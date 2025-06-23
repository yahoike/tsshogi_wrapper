// convert_kifu_to_sfen.mjs
import fs from "fs";
import { importKI2, importKIF, importCSA } from "tsshogi";
import iconv from "iconv-lite";
import path from "path";

const filePath = process.argv[2];
const ext = path.extname(filePath).toLowerCase();
const buffer = fs.readFileSync(filePath);
const content = iconv.decode(buffer, "cp932");

try {
  let record;

  if (ext === ".ki2") {
    record = importKI2(content);
  } else if (ext === ".kif") {
    record = importKIF(content);
  } else if (ext === ".csa") {
    record = importCSA(content);
  } else {
    throw new Error("未対応の拡張子です");
  }

  console.log(record.position.sfen);  // ← これが最も正しい書き方！

} catch (e) {
  console.error("変換失敗:", e.message);
  process.exit(1);
}
