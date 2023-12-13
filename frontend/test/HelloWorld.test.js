import { mount } from '@vue/test-utils'
import { describe, expect, it, test } from 'vitest'
import HelloWorld from '../src/components/HelloWorld.vue'



const wrapper = mount(HelloWorld)
const vm = wrapper.vm
  
describe("Testing HelloWorld.vue", () => {
    it("Render two buttons", () => {
      expect(wrapper.find('#button-start').isVisible()).toBe(true)
      expect(wrapper.find('#button-goto').isVisible()).toBe(true)
    })
})