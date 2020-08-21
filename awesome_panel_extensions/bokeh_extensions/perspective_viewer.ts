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

const perspectiveViewerClasses = [
  "perspective-viewer-material",
  "perspective-viewer-material-dark",
  "perspective-viewer-material-dense",
  "perspective-viewer-material-dense-dark",
  "perspective-viewer-vaporwave",
]
function is_not_perspective_class(item: any){
  return !perspectiveViewerClasses.includes(item);
}

function theme_to_class(theme: string): string {
  return "perspective-viewer-" + theme;
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
        this.connect(this.model.source.streaming, this.addData)
        this.connect(this.model.source.patching, this.updateOrAddData)

        this.connect(this.model.properties.columns.change, this.updateColumns)
        this.connect(this.model.properties.parsed_computed_columns.change, this.updateParsedComputedColumns)
        this.connect(this.model.properties.computed_columns.change, this.updateComputedColumns)
        this.connect(this.model.properties.column_pivots.change, this.updateColumnPivots)
        this.connect(this.model.properties.row_pivots.change, this.updateRowPivots)
        this.connect(this.model.properties.aggregates.change, this.updateAggregates)
        this.connect(this.model.properties.filters.change, this.updateFilters)
        this.connect(this.model.properties.plugin.change, this.updatePlugin)
        this.connect(this.model.properties.theme.change, this.updateTheme)
    }

    render(): void {
        super.render()
        console.log("render");
        const container = div({class: "pnx-tabulator"});
        const class_ = theme_to_class(this.model.theme);
        container.innerHTML="<perspective-viewer style='height:100%;width:100%;' class='" +class_+"'></perspective-viewer>"
        this.perspective_element=container.children[0]
        console.log(this.perspective_element);
        set_size(container, this.model)
        this.el.appendChild(container)

        this.setData();
        let viewer = this;
        function handleConfigurationChange(this: any): void {
          console.log("handleConfigurationChange")
          // this refers to the perspective-viewer element
          viewer.model.columns = this.columns; // Note columns is available as a property
          viewer.model.column_pivots =  JSON.parse(this.getAttribute("column-pivots"));
          viewer.model.parsed_computed_columns = JSON.parse(this.getAttribute("parsed-computed-columns"));
          viewer.model.computed_columns = JSON.parse(this.getAttribute("computed-columns"));
          viewer.model.row_pivots = JSON.parse(this.getAttribute("row-pivots"));
          viewer.model.aggregates = JSON.parse(this.getAttribute("aggregates"))
          viewer.model.sort = JSON.parse(this.getAttribute("sort"))
          viewer.model.filters = JSON.parse(this.getAttribute("filters"))

          // Perspective uses a plugin called 'debug' once in a while.
          // We don't send this back to the python side
          // Because then we would have to send include it in the list of plugins
          // the user can select.
          const plugin = this.getAttribute("plugin")
          if (plugin!=="debug"){viewer.model.plugin = this.getAttribute("plugin")}
        }
        this.perspective_element.addEventListener("perspective-config-update", handleConfigurationChange)
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

    updateAttribute(attribute: string, value: any, stringify: boolean): void {
      if (value === undefined || value===null || value === []) {
        return;
      }
      const old_value = this.perspective_element.getAttribute(attribute);

      if (stringify){
        value = JSON.stringify(value);
      }

      // We should only set the attribute if the new value is different to old_value
      // Otherwise we would get a recoursion/ stack overflow error
      if (old_value!==value){
        console.log(["updateAttribute", attribute, value, stringify, old_value, value])
        this.perspective_element.setAttribute(
          attribute,
          value
        );
      }
    }

    updateColumns(): void {this.updateAttribute("columns",this.model.columns,true,)}
    updateParsedComputedColumns(): void {this.updateAttribute("parsed-computed-columns",this.model.parsed_computed_columns,true,)}
    updateComputedColumns(): void {this.updateAttribute("computed-columns",this.model.computed_columns,true,)}
    updateColumnPivots(): void {this.updateAttribute("column-pivots",this.model.column_pivots,true,)}
    updateRowPivots(): void {this.updateAttribute("row-pivots",this.model.row_pivots,true,)}
    updateAggregates(): void {this.updateAttribute("aggregates",this.model.row_pivots,true,)}
    updateSort(): void {this.updateAttribute("sort",this.model.sort,true,)}
    updateFilters(): void {this.updateAttribute("sort",this.model.filters,true,)}
    updatePlugin(): void {this.updateAttribute("plugin",this.model.plugin,false,)}

    updateTheme(): void {
      // When you update class you have to be carefull
      // For example when the user is dragging an element then 'dragging' is added to the class value
      console.log("updateTheme")
      let el = this.perspective_element;
      let old_class = el.getAttribute("class");
      let new_class = this.toNewClass(old_class, this.model.theme);
      el.setAttribute("class", new_class)
    }

  private toNewClass(old_class: any, theme: string) {
    let new_classes = [];
    if (old_class != null) {
      new_classes = old_class.split(" ").filter(is_not_perspective_class);
    }
    new_classes.push(theme_to_class(theme));

    let new_class = new_classes.join(" ");
    return new_class;
  }
  }

export namespace PerspectiveViewer {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        source: p.Property<ColumnDataSource>,
        columns: p.Property<any[]>
        parsed_computed_columns: p.Property<any[]>
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
            parsed_computed_columns: [p.Array, []],
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
