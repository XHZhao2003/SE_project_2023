import { mount } from '@vue/test-utils'
import { describe, expect, it, test } from 'vitest'
import VenueSidebar from '../src/components/VenueSidebar.vue'


describe("Render all correct infomation", () => {
    it("Render all correct infomation", async () => {
        var wrapper = mount(VenueSidebar)
        await wrapper.setData({
            name: "test-name",
            opening_hours: "test-opening_hours",
            id: 1
        })
        var venueName = wrapper.find('#venuename')
        expect(venueName.text()).toEqual("test-name")
        var openinghours = wrapper.find('#opening-hours-content')
        expect(openinghours.text()).toEqual("test-opening_hours")
    })
})