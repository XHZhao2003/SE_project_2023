import { mount } from '@vue/test-utils'
import { test } from 'vitest'
import HelloWorld from '../src/components/HelloWorld.vue'

test("mount HelloWorld", () => {
  const wrapper = mount(HelloWorld)
})