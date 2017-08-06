import React from "react"

export default class Headline extends React.Component {
  render() {
    return (
        <div>
          <h1>{ this.props.children }
          </h1>
          <p> Your pet's box of treatures </p>
        </div>
    )
  }
}
