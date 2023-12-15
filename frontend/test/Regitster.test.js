import { mount } from '@vue/test-utils'  
import { describe, expect, it, test } from 'vitest'
import Register from '../src/components/Register.vue'

const wrapper = mount(Register)
const vm = wrapper.vm
const button = wrapper.find('#registerButton')
const form = wrapper.find('#registerForm')

vm.user.username = 'zxh123456'
vm.user.password = 'A123456'
vm.user.confirmpassword = 'A123456'
vm.user.email = '2100013129@st.pku.edu.cn'
await button.trigger('click')

test("Register with valid input", async () => {
    expect(vm.validRegister).toEqual(true) 
    vm.validRegister = false   
})

vm.user.email = '2981531232@qq.com'
await button.trigger('click')

test("Register with invalid email", async () => {
    expect(vm.validRegister).toEqual(false)
})

