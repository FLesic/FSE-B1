<template>
  <el-scrollbar height="100%" style="width: 100%; height: 100%">
    <div style="margin-top: 20px; margin-left:20px; font-size: 2em; font-weight: bold;">
      用户登录
    </div>
    <div style="width:45%;margin:0 auto; padding-top:5vh;">
      <div class="loginBox">
        <!-- 卡片标题 -->
        <div style="font-size: 25px; font-weight: bold;"></div>



        <!-- 卡片内容 -->
        <div style="height: 20px"></div>
        <div style="margin-left: 10px; text-align: start; font-size: 16px;">
          <div style="height: 25px"></div>
          <div style = "margin-left: 3vw; font-weight: bold; font-size: 1rem; margin-top: 5px;">
            账户名：
            <el-input v-model="account" style="width: 12.5vw; margin-left: 1rem" maxlength="18" clearable/>
          </div>
          <div style="height: 25px"></div>
          <div style = "margin-left: 4.3vw; font-weight: bold; font-size: 1rem; margin-top: 5px;">
            密码：
            <el-input v-model="password" style="width: 12.5vw; margin-left: 1rem" type="password" maxlength="20" clearable/>
          </div>
          <div style="height: 40px"></div>
        </div>
        <!-- 卡片操作 -->
        <div style="margin-top: 10px; display:flex; margin-left: 10rem;">
          <el-button type="primary"  @click="">
            登录
          </el-button>
        </div>
      </div>
    </div>

  </el-scrollbar>
</template>
<script>
import axios from "axios";
import { ElMessage } from 'element-plus'
export default{
  data(){
    return{
      account: "", // 用户登录，还不知道用什么
      password: "",
    }
  },
  methods: {},
  mounted() { // 当页面被渲染时
  }
}
</script>

<style scoped>
.loginBox {
  height: 300px;
  width: 400px;
  margin-top: 40px;
  margin-left: 27.5px;
  margin-right: 10px;
  padding: 7.5px;
  padding-right: 10px;
  padding-top: 15px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-align: center;
}
</style>