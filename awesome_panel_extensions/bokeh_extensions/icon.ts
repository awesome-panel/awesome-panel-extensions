import {AbstractIcon, AbstractIconView} from "@bokehjs/models/widgets/abstract_icon"
import * as p from "@bokehjs/core/properties"

// See https://stackoverflow.com/questions/494143/creating-a-new-dom-element-from-an-html-string-using-built-in-dom-methods-or-pro
/**
 * @param {String} HTML representing a single element
 * @return {Element}
 */
function htmlToElement(html: string) {
  var template = document.createElement('template');
  html = html.trim(); // Never return a text node of whitespace as the result
  template.innerHTML = html;
  return <HTMLElement>template.content.firstChild;
}

export class IconView extends AbstractIconView {
  model: Icon

  connect_signals(): void {
    super.connect_signals()
    this.connect(this.model.change, () => this.render())
  }

  render(): void {
    super.render()

    if (this.model.text===null && this.model.text===""){return}

    this.el.innerHTML=""
    const iconEl = htmlToElement(this.model.text)

    this.el.appendChild(iconEl)
    this.el.style.display = "inline"
    this.el.style.height = `${this.model.size}em`
    this.el.style.width = `${this.model.size}em`

    iconEl.style.verticalAlign = "middle"
    iconEl.style.height = `${this.model.size}em`
    iconEl.style.width = `${this.model.size}em`
    iconEl.style.fill = this.model.fill_color

    if (this.model.spin_duration>0){
      // See https://codepen.io/eveness/pen/BjLaoa
      const animationDuration = `${this.model.spin_duration}ms`

      iconEl.style.setProperty("-webkit-animation-name", "spin")
      iconEl.style.setProperty("-webkit-animation-duration", animationDuration)
      iconEl.style.setProperty("-webkit-animation-iteration-count", "infinite")
      iconEl.style.setProperty("-webkit-animation-timing-function", "linear")
      iconEl.style.setProperty("-moz-animation-name", "spin")
      iconEl.style.setProperty("-moz-animation-duration", animationDuration)
      iconEl.style.setProperty("-moz-animation-iteration-count", "infinite")
      iconEl.style.setProperty("-moz-animation-timing-function", "linear")
      iconEl.style.setProperty("-ms-animation-name", "spin")
      iconEl.style.setProperty("-ms-animation-duration", animationDuration)
      iconEl.style.setProperty("-ms-animation-iteration-count", "infinite")
      iconEl.style.setProperty("-ms-animation-timing-function", "linear")
      iconEl.style.setProperty("animation-name", "spin")
      iconEl.style.setProperty("animation-duration", animationDuration)
      iconEl.style.setProperty("animation-iteration-count", "infinite")
      iconEl.style.setProperty("animation-timing-function", "linear")

    }

    iconEl.classList.add("icon")
    if (this.model.label!=null && this.model.label!==""){
      const label = this.model.label.toLowerCase().replace(" ", "")
      iconEl.classList.add(`icon-${label}`)
    }
  }
}

export namespace Icon {
  export type Attrs = p.AttrsOf<Props>

  export type Props = AbstractIcon.Props & {
    label: p.Property<string>;
    text: p.Property<string>;
    size: p.Property<number>;
    fill_color: p.Property<string>;
    spin_duration: p.Property<number>;
  }
}

export interface Icon extends Icon.Attrs {}

export class Icon extends AbstractIcon {
  properties: Icon.Props

  constructor(attrs?: Partial<Icon.Attrs>) {
    super(attrs)
  }

  static __module__ = "awesome_panel_extensions.bokeh_extensions.icon"

  static init_Icon(): void {
    this.prototype.default_view = IconView

    this.define<Icon.Props>({
        label: [p.String, ],
        text: [p.String, ],
        size:      [ p.Number, 1.0 ],
        fill_color: [ p.String, "currentColor"],
        spin_duration: [ p.Int, 0 ],
    })
  }
}