import { mount } from '@vue/test-utils'  
import { describe, expect, it, test } from 'vitest'
import Roadsidebar from '../src/components/Roadsidebar.vue'


describe("Description of Road with different crowding", ()=>{
    it('Crowding = 1', ()=>{
        var wrapper = mount(Roadsidebar, {
            props:{
                name: "Road1",
                crowding: 1,
                road_id: 1
            }
        })
        var vm = wrapper.vm
        var description = wrapper.find('#description')
        expect(description.text()).toEqual("路况良好，顺畅通行！")
    })
    it('Crowding = 2', ()=>{
        var wrapper = mount(Roadsidebar, {
            props:{
                name: "Road1",
                crowding: 2,
                road_id: 1
            }
        })
        var vm = wrapper.vm
        var description = wrapper.find('#description')
        expect(description.text()).toEqual("路况适中，您可以从这里通行")
    })
    it('Crowding = 3', ()=>{
        var wrapper = mount(Roadsidebar, {
            props:{
                name: "Road1",
                crowding: 3,
                road_id: 1
            }
        })
        var vm = wrapper.vm
        var description = wrapper.find('#description')
        expect(description.text()).toEqual("道路拥挤，您最好选择绕行")
    })
    it('Crowding = 4', ()=>{
        var wrapper = mount(Roadsidebar, {
            props:{
                name: "Road1",
                crowding: 4,
                road_id: 1
            }
        })
        var vm = wrapper.vm
        var description = wrapper.find('#description')
        expect(description.text()).toEqual("严重堵塞，您不会想来这里的！")
    })
})

describe("Send feedback", ()=>{
    it("Send feedback", async ()=>{
        var wrapper = mount(Roadsidebar, {
            props:{
                name: "Road1",
                crowding: 1,
                road_id: 1
            }
        })
        var vm = wrapper.vm
        await wrapper.find('#openFeedbackButton').trigger('click')
        var buttons = wrapper.find('.feedbackbutton')
        expect(buttons.isVisible()).toBe(true)
    })
})