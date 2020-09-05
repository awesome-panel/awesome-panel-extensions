
import {Button, ButtonView} from "@bokehjs/models/widgets/button"

import * as p from "@bokehjs/core/properties"
// Browse the fast-button api here  https://explore.fast.design/components/fast-button
export class FastButtonView extends ButtonView {
  model: FastButton;

  _render_button(..._: (string | HTMLElement)[]): HTMLButtonElement {
    const button = <any>document.createElement("fast-button");
    button.innerText = this.model.label;
    button.disabled = this.model.disabled;
    button.appearance = this.model.appearance;
    button.autofocus = this.model.autofocus;
    button.style.width="100%"
    button.style.height="100%"
    return <HTMLButtonElement>button
  }
}

export namespace FastButton {
  export type Attrs = p.AttrsOf<Props>

  export type Props = Button.Props & {
    appearance: p.Property<string>;
    autofocus: p.Property<boolean>;
    }
}

export interface FastButton extends FastButton.Attrs {}

export class FastButton extends Button {
  properties: FastButton.Props
  // __view_type__: FastButtonView

  constructor(attrs?: Partial<FastButton.Attrs>) {
    super(attrs)
  }

  static __module__ = "awesome_panel_extensions.bokeh_extensions.fast_button"

  static init_FastButton(): void {
    this.prototype.default_view = FastButtonView

    this.define<FastButton.Props>({
        appearance: [p.String, ],
        autofocus: [p.Boolean, ],
    })
  }
}