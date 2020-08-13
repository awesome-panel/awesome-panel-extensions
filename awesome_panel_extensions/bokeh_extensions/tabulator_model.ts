// See https://docs.bokeh.org/en/latest/docs/reference/models/layouts.html
import { HTMLBox, HTMLBoxView } from "models/layouts/html_box"
import {div} from "core/dom"
// See https://docs.bokeh.org/en/latest/docs/reference/core/properties.html
import * as p from "core/properties";
import {ColumnDataSource} from "models/sources/column_data_source";

export function set_size(el: HTMLElement, model: HTMLBox): void {
    let width_policy = model.width != null ? "fixed" : "fit"
    let height_policy = model.height != null ? "fixed" : "fit"
    const {sizing_mode} = model
    if (sizing_mode != null) {
      if (sizing_mode == "fixed")
        width_policy = height_policy = "fixed"
      else if (sizing_mode == "stretch_both")
        width_policy = height_policy = "max"
      else if (sizing_mode == "stretch_width")
        width_policy = "max"
      else if (sizing_mode == "stretch_height")
        height_policy = "max"
      else {
        switch (sizing_mode) {
        case "scale_width":
          width_policy = "max"
          height_policy = "min"
          break
        case "scale_height":
          width_policy = "min"
          height_policy = "max"
          break
        case "scale_both":
          width_policy = "max"
          height_policy = "max"
          break
        default:
          throw new Error("unreachable")
        }
      }
    }
    if (width_policy == "fixed" && model.width)
      el.style.width = model.width + "px";
    else if (width_policy == "max")
      el.style.width = "100%";

    if (height_policy == "fixed" && model.height)
      el.style.height = model.height + "px";
    else if (height_policy == "max")
      el.style.height = "100%";
  }

function transform_cds_to_records(cds: ColumnDataSource): any {
  const data: any = []
  const columns = cds.columns()
  const cdsLength = cds.get_length()
  if (columns.length === 0||cdsLength === null) {
    return [];
  }
  for (let i = 0; i < cdsLength; i++) {
    const item: any = {}
    for (const column of columns) {
      let array: any = cds.get_array(column);
      const shape = array[0].shape == null ? null : array[0].shape;
      if ((shape != null) && (shape.length > 1) && (typeof shape[0] == "number"))
        item[column] = array.slice(i*shape[1], i*shape[1]+shape[1])
      else
        item[column] = array[i]
    }
    data.push(item)
  }
  return data
}

function getConfiguration(model: TabulatorModel): any {
  let data = model.data
  if (data ===null){
    return model.configuration;
  }
  else {
    console.log("adding data to configuration");
    let configuration = model.configuration;
    if (!configuration){
      configuration={}
    };
    data = transform_cds_to_records(data)
    return {...configuration, "data": data};
  }

}

declare const Tabulator: any;

// The view of the Bokeh extension/ HTML element
// Here you can define how to render the model as well as react to model changes or View events.
export class TabulatorModelView extends HTMLBoxView {
    model: TabulatorModel;
    tabulator: any;
    // objectElement: any // Element

    connect_signals(): void {
        super.connect_signals()

        this.connect(this.model.properties.configuration.change, () => {
            this.render();
        })
        this.connect(this.model.properties.data.change, () => {
          this.setData();
        })
        this.connect(this.model.data.change, () => this.setData())
        // this.connect(this.model.data.properties.data.change, () => this.setData())
        this.connect(this.model.data.streaming, () => this.addData())
        this.connect(this.model.data.patching, () => this.updateOrAddData())
    }

    render(): void {
        super.render()
        console.log("render");
        console.log(this.model);
        const container = div({class: "pnx-tabulator"});
        set_size(container, this.model)
        console.log(this.model.configuration);
        let configuration = getConfiguration(this.model);
        this.tabulator = new Tabulator(container, configuration)
        this.el.appendChild(container)
        // this.objectElement.addEventListener("click", () => {this.model.clicks+=1;}, false)
    }

    after_layout(): void {
        console.log("redraw");
        console.log(this.tabulator);
        super.after_layout()
        this.tabulator.redraw(true);
    }

    setData(): void {
      console.log("setData");
      let data = transform_cds_to_records(this.model.data);
      this.tabulator.setData(data);
    }

    addData(): void {
      console.log("addData");
      let data = transform_cds_to_records(this.model.data);
      this.tabulator.setData(data);
    }

    updateOrAddData(): void {
      console.log("updateData");
      let data = transform_cds_to_records(this.model.data);
      this.tabulator.setData(data);
    }


}

export namespace TabulatorModel {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        configuration: p.Property<any>,
        data: p.Property<ColumnDataSource>,
        selected_indicies: p.Property<number[]>
    }
}

export interface TabulatorModel extends TabulatorModel.Attrs { }

// The Bokeh .ts model corresponding to the Bokeh .py model
export class TabulatorModel extends HTMLBox {
    properties: TabulatorModel.Props

    constructor(attrs?: Partial<TabulatorModel.Attrs>) {
        super(attrs)
    }

    static init_TabulatorModel(): void {
        this.prototype.default_view = TabulatorModelView;

        this.define<TabulatorModel.Props>({
            configuration: [p.Any, ],
            data: [p.Any, ],
            selected_indicies: [p.Any, []]
        })
    }
}
