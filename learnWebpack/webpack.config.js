module.exports = {
  // entry エントリーポイント
  entry: "./src/index.js",
  output: {
    // output.path 出力ディレクトリ
    path: `${__dirname}/dist`,
    // output.filename 出力ファイル名
    filename: "main.js",
  }
}