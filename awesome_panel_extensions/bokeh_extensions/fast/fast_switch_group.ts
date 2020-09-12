
import {CheckboxGroup, CheckboxGroupView} from "@bokehjs/models/widgets/checkbox_group"
import {bk_inline} from "@bokehjs/styles/mixins"
import {bk_input_group} from "@bokehjs/styles/widgets/inputs"

import {div} from "@bokehjs/core/dom"
import {includes} from "@bokehjs/core/util/array"

import * as p from "@bokehjs/core/properties"
// Browse the fast-switch api here https://explore.fast.design/components/fast-switch
export class FastSwitchGroupView extends CheckboxGroupView {
  model: FastSwitchGroup;

  render(): void {
    // Cannot call super.render() as this will add the group twice
    // super.render()

    const group = div({class: [bk_input_group, this.model.inline ? bk_inline : null]})
    this.el.innerHTML="";
    this.el.appendChild(group)

    const {active, labels} = this.model
    this._inputs = []
    for (let i = 0; i < labels.length; i++) {
      let FastSwitch = <any>document.createElement("fast-switch")
      if (this.model.readonly)
        // Setting the property did not work for me. Thus I set the attribute
        FastSwitch.setAttribute("readonly", true)
      FastSwitch.innerHTML = labels[i]
      FastSwitch.innerHTML = labels[i]
      const fastSwitch = <HTMLInputElement>FastSwitch

      fastSwitch.value = `${i}`
      // const checkbox = input({type: `checkbox`, value: `${i}`})
      fastSwitch.addEventListener("change", () => this.change_active(i))
      this._inputs.push(fastSwitch)

      if (this.model.disabled)
        fastSwitch.disabled = true

      if (includes(active, i))
        fastSwitch.checked = true


      const checked_message = document.createElement("span")
      checked_message.setAttribute("slot", "checked-message")
      checked_message.innerHTML=this.model.checked_message
      fastSwitch.appendChild(checked_message)

      const unchecked_message = document.createElement("span")
      unchecked_message.setAttribute("slot", "unchecked-message")
      unchecked_message.innerHTML=this.model.unchecked_message
      fastSwitch.appendChild(unchecked_message)

      // const label_el = label({}, checkbox, span({}, labels[i]))
      group.appendChild(fastSwitch)
    }
  }
}

export namespace FastSwitchGroup {
  export type Attrs = p.AttrsOf<Props>

  export type Props = CheckboxGroup.Props & {
    readonly: p.Property<boolean>;
    checked_message: p.Property<string>;
    unchecked_message: p.Property<string>;
    }
}

export interface FastSwitchGroup extends FastSwitchGroup.Attrs {}

export class FastSwitchGroup extends CheckboxGroup {
  properties: FastSwitchGroup.Props

  constructor(attrs?: Partial<FastSwitchGroup.Attrs>) {
    super(attrs)
  }

  static __module__ = "awesome_panel_extensions.bokeh_extensions.fast.fast_switch_group"

  static init_FastSwitchGroup(): void {
    this.prototype.default_view = FastSwitchGroupView

    this.define<FastSwitchGroup.Props>({
        readonly: [p.Boolean, ],
        checked_message: [p.String, ],
        unchecked_message: [p.String, ],
    })
  }
}