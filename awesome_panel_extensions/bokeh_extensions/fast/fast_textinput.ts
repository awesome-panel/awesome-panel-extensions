import {TextInput} from "@bokehjs/models/widgets/text_input"
import {InputWidgetView} from "@bokehjs/models/widgets/input_widget"

import * as p from "@bokehjs/core/properties"

// I tried to inherit from TextInputView but I could not
// get it working. It created two textinputs.
export class FastTextInputView extends InputWidgetView {
    model: FastTextInput

    protected input_el: HTMLInputElement

    connect_signals(): void {
      super.connect_signals()
      this.connect(this.model.properties.name.change, () => this.input_el.name = this.model.name ?? "")
      this.connect(this.model.properties.value.change, () => {this.input_el.value = this.model.value;console.log("value")})
      this.connect(this.model.properties.value_input.change, () => {this.input_el.value = this.model.value_input;console.log("value_input")})
      this.connect(this.model.properties.disabled.change, () => this.input_el.disabled = this.model.disabled)
      this.connect(this.model.properties.placeholder.change, () => this.input_el.placeholder = this.model.placeholder)

      this.connect(this.model.properties.appearance.change, () => this.input_el_any.appearance = this.model.appearance)
      this.connect(this.model.properties.autofocus.change, () => this.input_el_any.autofocus = this.model.autofocus)
      this.connect(this.model.properties.type_of_text.change, () => this.input_el_any.type = this.model.type_of_text)
      this.connect(this.model.properties.maxlength.change, () => this.input_el_any.maxlength = this.model.maxlength)
      this.connect(this.model.properties.minlength.change, () => this.input_el_any.minlength = this.model.minlength)
      this.connect(this.model.properties.pattern.change, () => this.input_el_any.pattern = this.model.pattern)
      // Could not get size working. It raises an error
      // this.connect(this.model.properties.size.change, () => this.input_el_any.size = this.model.size)
      this.connect(this.model.properties.spellcheck.change, () => this.input_el_any.spellcheck = this.model.spellcheck)
      this.connect(this.model.properties.required.change, () => this.input_el_any.required = this.model.required)
      // Could not get readonly working as a property.
      // https://github.com/microsoft/fast/issues/3852
      this.connect(this.model.properties.readonly.change, () => this.input_el_any.setAttribute("readonly", this.model.readonly))
    }


    public get input_el_any() : any {
      return <any>this.input_el;
    }


    render(): void {
      super.render()

      const fastTextField = <any>document.createElement("fast-text-field")
      this.input_el = <HTMLInputElement>fastTextField;
      this.input_el.className="bk-fast-input"
      this.input_el.addEventListener("change", () => this.change_input())
      this.input_el.addEventListener("input",  () => this.change_input_oninput())
      this.group_el.appendChild(this.input_el)

      // For some unknown reason we need to set these properties after the above
      // Otherwise for example the value is reset to ""
      fastTextField.name = this.model.name;
      fastTextField.value = this.model.value;
      fastTextField.appearance = this.model.appearance;
      fastTextField.autofocus = this.model.autofocus;
      fastTextField.placeholder = this.model.placeholder;
      fastTextField.disabled = this.model.disabled;
      fastTextField.type = this.model.type_of_text;
      fastTextField.maxlength = this.model.maxlength;
      fastTextField.minlength = this.model.minlength;
      fastTextField.pattern = this.model.pattern;
      // Could not get size working. It raises an error.
      // fastTextField.size = this.model.size;
      fastTextField.spellcheck = this.model.spellcheck;
      fastTextField.required = this.model.required;
      fastTextField.disabled = this.model.disabled;
      fastTextField.setAttribute("readonly", this.model.readonly)
    }

    change_input(): void {
      this.model.value = this.input_el.value
      super.change_input()
    }

    change_input_oninput(): void {
      this.model.value_input = this.input_el.value
      super.change_input()
    }
  }

export namespace FastTextInput {
  export type Attrs = p.AttrsOf<Props>

  export type Props = TextInput.Props & {
      // name inherited
      // value inherited
      appearance: p.Property<string>;
      autofocus: p.Property<boolean>;
      // placeholder inherited
      type_of_text: p.Property<string>;
      maxlength: p.Property<number>;
      minlength: p.Property<number>;
      pattern: p.Property<string>;
      size: p.Property<number>;
      spellcheck: p.Property<boolean>;
      required: p.Property<boolean>;
      // disabled inherited
      readonly: p.Property<boolean>;
  }
}

export interface FastTextInput extends FastTextInput.Attrs {}

export class FastTextInput extends TextInput {
  properties: FastTextInput.Props

  constructor(attrs?: Partial<FastTextInput.Attrs>) {
    super(attrs)
  }

  static __module__ = "awesome_panel_extensions.bokeh_extensions.fast.fast_textinput"

  static init_FastTextInput(): void {
    this.prototype.default_view = FastTextInputView

    this.define<FastTextInput.Props>({
        // name inherited
        // value inherited
        appearance: [p.String, ],
        autofocus: [p.Boolean, ],
        // placeholder inherited
        type_of_text: [p.String, ],
        maxlength: [p.Number, ],
        minlength: [p.Number, ],
        pattern: [p.String, ],
        size: [p.Any, ],
        spellcheck: [p.Boolean, ],
        required: [p.Boolean, ],
        // disabled inherited
        readonly: [p.Boolean, ],
    })
  }
}