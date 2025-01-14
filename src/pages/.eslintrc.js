module.exports = {
  root: true,
  extends: ['@bkui/eslint-config-bk/vue'],
  globals: {
    NODE_ENV: false,
  },
  parserOptions: {
    parser: 'babel-eslint',
    sourceType: 'module',
    ecmaFeatures: {
        legacyDecorators: true
    }
  },

  rules: {
    'no-param-reassign': 'off',
    'prefer-destructuring': 'off',
    'no-underscore-dangle': 'off',
    'no-restricted-syntax': 'off',
    'array-callback-return': 'off',
    'no-nested-ternary': 'off',
    'arrow-body-style': 'off',
    'no-restricted-properties': 'off',
 },
};
