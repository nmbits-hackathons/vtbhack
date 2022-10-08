<template>
  <button class="button__wrapper" data-variant="primary">
    <slot></slot>
  </button>
</template>

<style lang="scss" scoped>
.button__wrapper {
  cursor: pointer;
  
  transition: var(--transition);
  
  padding: 16px 24px;
  border-radius: 16px;
  
  font-family: "Inter", serif;
  font-weight: 500;
  font-size: 18px;
  line-height: 22px;
  letter-spacing: -0.02em;

  $variants: primary, secondary, tertiary;

    @each $variant in $variants {
      &[data-variant="#{$variant}"] {
        background: rgb(var(--button-#{$variant}));
        color: rgb(var(--button-#{$variant}-text));
        border: var(--button-#{$variant}-border, 0px solid);

        &:hover {
          background: rgb(var(--button-#{$variant}-hover));
        }
      }
    }
}
</style>