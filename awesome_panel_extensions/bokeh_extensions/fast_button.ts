
import {Button, ButtonView} from "@bokehjs/models/widgets/button"

import * as p from "@bokehjs/core/properties"

export class FastButtonView extends ButtonView {
  model: FastButton;
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