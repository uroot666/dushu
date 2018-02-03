//index.js
//获取应用实例
var app = getApp()
Page({
  data: {},
  //事件处理函数
  bindViewInput: function(res) {
    var that = this
    this.setData({
      inputTxt: ''
    }),
    wx.request({
      url: 'https://dushu.atimo.cn/weixin/book/',
      data: {
        barcode: res.detail.value
      },
      success: function(res) {
        wx.hideLoading()
        console.log(res.data)
        that.setData({
          barcodeData:res.data.data
        });
      }
    })
  },
  onLoad: function () {
    console.log('onLoad')    
  }
})
