// Bokeh model for perspective-viewer
// See https://github.com/finos/perspective/tree/master/packages/perspective-viewer

// See https://docs.bokeh.org/en/latest/docs/reference/models/layouts.html
import { HTMLBox, HTMLBoxView } from "@bokehjs/models/layouts/html_box"
import {div} from "@bokehjs/core/dom"
// See https://docs.bokeh.org/en/latest/docs/reference/core/properties.html
import * as p from "@bokehjs/core/properties";
import {ColumnDataSource} from "@bokehjs/models/sources/column_data_source";

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

// The view of the Bokeh extension/ HTML element
// Here you can define how to render the model as well as react to model changes or View events.
export class PerspectiveViewerView extends HTMLBoxView {
    model: PerspectiveViewer;
    perspective_element: any;

    connect_signals(): void {
        super.connect_signals()

        this.connect(this.model.source.properties.data.change, () => {
          this.setData();
        })
        this.connect(this.model.source.streaming, () => this.addData())
        this.connect(this.model.source.patching, () => this.updateOrAddData())

        this.connect(this.model.properties.columns.change, () => this.updateColumns())
    }

    render(): void {
        super.render()
        console.log("render");
        const container = div({class: "pnx-tabulator"});
        container.innerHTML="<perspective-viewer style='height:100%;width:100%;'></perspective-viewer>"
        this.perspective_element=container.children[0]
        console.log(this.perspective_element);
        set_size(container, this.model)
        this.el.appendChild(container)

        let viewer = this;
        function handleConfigurationChange(this: any): void {
            console.log("handleConfigurationChange")
            // this is the perspective-viewer element
            viewer.model.columns = this.columns;
            console.log(this.columnPivots);
            // viewer.model.column_pivots = this.column_pivots;
            console.log(this.computedColumns);
            // viewer.model.computed_columns = this.computed_columns;
            // viewer.model.row_pivots = this.row_pivots;
            // viewer.model.aggregates = this.aggregates;
            console.log(this.sort);
            viewer.model.sort = this.sort;
            // viewer.model.filters = this.filters;
            // viewer.model.plugin = this.plugin;
        }
        this.perspective_element.addEventListener("perspective-config-update", handleConfigurationChange)

        this.setData();

        this.updateColumns();
    }

    setData(): void {
      console.log("setData");
      let data = transform_cds_to_records(this.model.source);
      this.perspective_element.load(data)
    }

    addData(): void {
      console.log("addData");
      // I need to find out how to only load the streamed data
      // using this.perspective_element.update
      this.setData();
    }

    updateOrAddData(): void {
      console.log("updateData");
      // I need to find out how to only load the patched data
      // using this.perspective_element.update
      this.setData();
    }

    updateColumns(): void {
        if (this.model.columns === undefined || this.model.columns.length == 0) {
            return;
        }

        console.log("updateColumns");
        // I need to find out how to only load the patched data
        // using this.perspective_element.update
        const columns = JSON.stringify(this.model.columns)
        this.perspective_element.columns = columns;
      }
}

export namespace PerspectiveViewer {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        source: p.Property<ColumnDataSource>,
        columns: p.Property<any[]>
        computed_columns: p.Property<any[]>
        column_pivots: p.Property<any[]>
        row_pivots: p.Property<any[]>
        aggregates: p.Property<any>
        sort: p.Property<any[]>
        filters: p.Property<any[]>
        plugin: p.Property<any>
        theme: p.Property<any>
    }
}

export interface PerspectiveViewer extends PerspectiveViewer.Attrs { }

// The Bokeh .ts model corresponding to the Bokeh .py model
export class PerspectiveViewer extends HTMLBox {
    properties: PerspectiveViewer.Props

    constructor(attrs?: Partial<PerspectiveViewer.Attrs>) {
        super(attrs)
    }

    static __module__ = "awesome_panel_extensions.bokeh_extensions.perspective_viewer"

    static init_PerspectiveViewer(): void {
        this.prototype.default_view = PerspectiveViewerView;

        this.define<PerspectiveViewer.Props>({
            source: [p.Any, ],
            columns: [p.Array, []],
            computed_columns: [p.Array, []],
            column_pivots: [p.Array, []],
            row_pivots: [p.Array, []],
            aggregates: [p.Any, ],
            sort: [p.Array, []],
            filters: [p.Array, []],
            plugin: [p.String, ],
            theme: [p.String, ],
        })
    }
}
