import {TextAreaInput} from "@bokehjs/models/widgets/textarea_input"
import {InputWidgetView} from "@bokehjs/models/widgets/input_widget"

import * as p from "@bokehjs/core/properties"

// I tried to inherit from TextAreaInputView but I could not
// get it working. It created two textareainputs.
export class FastTextAreaInputView extends InputWidgetView {
    model: FastTextAreaInput

    protected input_el: HTMLTextAreaElement

    public get input_el_any() : any {
      return <any>this.input_el;
    }

    connect_signals(): void {
      super.connect_signals()
      this.connect(this.model.properties.name.change, () => this.input_el.name = this.model.name ?? "")
      this.connect(this.model.properties.value.change, () => {this.input_el.value = this.model.value;})
      this.connect(this.model.properties.disabled.change, () => this.input_el.disabled = this.model.disabled)
      this.connect(this.model.properties.placeholder.change, () => this.input_el.placeholder = this.model.placeholder)
      this.connect(this.model.properties.rows.change, () => this.input_el.rows = this.model.rows)
      this.connect(this.model.properties.cols.change, () => this.input_el.cols = this.model.cols)
      this.connect(this.model.properties.max_length.change, () => this.input_el_any.setAttribute("maxlength", this.model.max_length))

      this.connect(this.model.properties.appearance.change, () => this.input_el_any.appearance = this.model.appearance)
      this.connect(this.model.properties.autofocus.change, () => this.input_el_any.autofocus = this.model.autofocus)
      this.connect(this.model.properties.resize.change, () => this.input_el_any.resize = this.model.resize)
      this.connect(this.model.properties.spellcheck.change, () => this.input_el_any.spellcheck = this.model.spellcheck)
      this.connect(this.model.properties.min_length.change, () => this.input_el_any.setAttribute("minlength", this.model.min_length))
      this.connect(this.model.properties.required.change, () => this.input_el_any.required = this.model.required)
      // Could not get readonly working as a property.
      // https://github.com/microsoft/fast/issues/3852
      this.connect(this.model.properties.readonly.change, () => {
        if (this.model.readonly===true){
          this.input_el_any.setAttribute("readonly", "")
        } else {
          this.input_el_any.removeAttribute("readonly")
        }
      })
    }


    render(): void {
      super.render()

      const fastTextArea = <any>document.createElement("fast-text-area")
      this.input_el = <HTMLTextAreaElement>fastTextArea;
      this.input_el.className="bk-fast-input"
      this.input_el.addEventListener("change", () => this.change_input())
      this.group_el.appendChild(this.input_el)

      // For some unknown reason we need to set these properties after the above
      // Otherwise for example the value is reset to ""
      fastTextArea.name = this.model.name;
      fastTextArea.value = this.model.value;
      fastTextArea.disabled = this.model.disabled;
      fastTextArea.placeholder = this.model.placeholder;
      fastTextArea.cols = this.model.cols;
      fastTextArea.rows = this.model.rows;
      if (this.model.max_length!=null)
        fastTextArea.setAttribute("maxlength", this.model.max_length);


      fastTextArea.appearance = this.model.appearance;
      fastTextArea.autofocus = this.model.autofocus;
      fastTextArea.resize = this.model.resize;
      fastTextArea.spellcheck = this.model.spellcheck;
      if (this.model.min_length!=null)
        fastTextArea.setAttribute("minlength", this.model.min_length);
      fastTextArea.required = this.model.required;
      if (this.model.readonly===true)
        fastTextArea.setAttribute("readonly", "");
    }

    change_input(): void {
      this.model.value = this.input_el.value
      super.change_input()
    }
  }

export namespace FastTextAreaInput {
  export type Attrs = p.AttrsOf<Props>

  export type Props = TextAreaInput.Props & {
      // name inherited
      // value inherited
      // placeholder inherited
      // max_length inherited
      // disabled inherited
      // cols inherited
      // rows inherited
      appearance: p.Property<string>;
      autofocus: p.Property<boolean>;
      resize: p.Property<string>;
      spellcheck: p.Property<boolean>;
      min_length: p.Property<number>;
      required: p.Property<boolean>;
      readonly: p.Property<boolean>;
  }
}

export interface FastTextAreaInput extends FastTextAreaInput.Attrs {}

export class FastTextAreaInput extends TextAreaInput {
  properties: FastTextAreaInput.Props

  constructor(attrs?: Partial<FastTextAreaInput.Attrs>) {
    super(attrs)
  }

  static __module__ = "awesome_panel_extensions.bokeh_extensions.fast.fast_textarea_input"

  static init_FastTextAreaInput(): void {
    this.prototype.default_view = FastTextAreaInputView

    this.define<FastTextAreaInput.Props>({
        // name inherited
        // value inherited
        // placeholder inherited
        // max_length inherited
        // disabled inherited
        // cols inherited
        // rows inherited
        appearance: [p.String, ],
        autofocus: [p.Boolean, ],
        resize: [p.String, ],
        spellcheck: [p.Boolean, ],
        min_length: [p.Number, ],
        required: [p.Boolean, ],
        readonly: [p.Boolean, ],
    })
  }
}