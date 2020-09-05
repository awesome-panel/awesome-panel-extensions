
import {CheckboxGroup, CheckboxGroupView} from "@bokehjs/models/widgets/checkbox_group"

import * as p from "@bokehjs/core/properties"
// Browse the fast-button api here  https://explore.fast.design/components/fast-button
export class FastCheckboxGroupView extends CheckboxGroupView {
  model: FastCheckboxGroup;
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

    this.define<FastCheckboxGroup.Props>({
        readonly: [p.Boolean, ],
    })
  }
}