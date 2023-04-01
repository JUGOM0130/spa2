const {
  defineConfig
} = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  /**
   * 以下追加した部分
   * 各ページのエントリポイントとなる
   */
  pages: {
    //下記キーがURLのエントリポイント名となる
    index: {
      entry: 'src/main.js', // エントリーポイントとなるjs
      template: 'public/index.html', // テンプレートのHTML
      filename: 'index.html', // build時に出力されるファイル名
    },
    code: {
      entry: 'src/pages/code/main.js', // エントリーポイントとなるjs
      template: 'public/code.html', // テンプレートのHTML
      filename: 'code.html', // build時に出力されるファイル名
      titel: '管理メニュー'
    },
    staff: {
      entry: 'src/pages/staff/main.js',
      template: 'public/staff.html',
      filename: 'staff.html',
    },
    tree: {
      entry: 'src/pages/tree/main.js',
      template: 'public/tree.html',
      filename: 'tree.html',
    },
  },
  devServer: {
    historyApiFallback: {
      rewrites: [{
          from: /\/index/,
          to: '/index.html'
        },
        {
          from: /\/code/,
          to: '/code.html'
        }
      ]
    }
  },
  pluginOptions: {
    vuetify: {
      // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
    }
  }
})
