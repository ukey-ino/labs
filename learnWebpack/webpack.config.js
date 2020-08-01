module.exports = {
  // mode webpackするときの圧縮モード
  //   development: 開発用 
  //   production:  本番用 
  mode: "development",
  // entry エントリーポイント
  entry: "./src/index.js",
  output: {
    // output.path 出力ディレクトリ
    path: `${__dirname}/dist`,
    // output.filename 出力ファイル名
    filename: "main.js",
  },
  devServer: {
    // devServer.contentBase Webサーバーのコンテンツディレクトリ
    contentBase: "dist",
    // devServer.open ブラウザを自動で開く
    open: true,
  }
}