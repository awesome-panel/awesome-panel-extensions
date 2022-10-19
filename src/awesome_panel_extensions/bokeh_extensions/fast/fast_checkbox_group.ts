
import {CheckboxGroup, CheckboxGroupView} from "@bokehjs/models/widgets/checkbox_group"
import * as inputs from "@bokehjs/styles/widgets/inputs.css"

import {div} from "@bokehjs/core/dom"
import {includes} from "@bokehjs/core/util/array"

import * as p from "@bokehjs/core/properties"
// Browse the fast-button api here  https://explore.fast.design/components/fast-button
export class FastCheckboxGroupView extends CheckboxGroupView {
  model: FastCheckboxGroup;

  render(): void {
    // Cannot call super.render() as this will add the group twice
    // super.render()

    const group = div({class: [inputs.input_group, this.model.inline ? inputs.inline : null]})
    this.el.innerHTML="";
    this.el.appendChild(group)

    const {active, labels} = this.model
    this._inputs = []
    for (let i = 0; i < labels.length; i++) {
      let fastCheckBox = <any>document.createElement("fast-checkbox")
      if (this.model.readonly)
        // Setting the property did not work for me. Thus I set the attribute
        fastCheckBox.setAttribute("readonly", true)
      fastCheckBox.innerHTML = labels[i]
      const checkbox = <HTMLInputElement>fastCheckBox

      checkbox.value = `${i}`
      // const checkbox = input({type: `checkbox`, value: `${i}`})
      checkbox.addEventListener("change", () => this.change_active(i))
      this._inputs.push(checkbox)

      if (this.model.disabled)
        checkbox.disabled = true

      if (includes(active, i))
        checkbox.checked = true

      // const label_el = label({}, checkbox, span({}, labels[i]))
      group.appendChild(checkbox)
    }
  }
}

export namespace FastCheckboxGroup {
  export type Attrs = p.AttrsOf<Props>

  export type Props = CheckboxGroup.Props & {
    readonly: p.Property<boolean>;
    }
}

export interface FastCheckboxGroup extends FastCheckboxGroup.Attrs {}

export class FastCheckboxGroup extends CheckboxGroup {
  properties: FastCheckboxGroup.Props

  constructor(attrs?: Partial<FastCheckboxGroup.Attrs>) {
    super(attrs)
  }

  static __module__ = "awesome_panel_extensions.bokeh_extensions.fast.fast_checkbox_group"

  static init_FastCheckboxGroup(): void {
    this.prototype.default_view = FastCheckboxGroupView

    this.define<FastCheckboxGroup.Props>(({Boolean}) => ({
        readonly: [Boolean, ],
    }))
  }
}