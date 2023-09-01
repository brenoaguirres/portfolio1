(
    XL_CELL_EMPTY,  # 0
    XL_CELL_TEXT,  # 1
    XL_CELL_NUMBER,  # 2
    XL_CELL_DATE,  # 3
    XL_CELL_BOOLEAN,  # 4
    XL_CELL_ERROR,  # 5
    XL_CELL_BLANK  # 6
) = range(7)

ctype_text = {
    XL_CELL_EMPTY: 'empty',
    XL_CELL_TEXT: 'text',
    XL_CELL_NUMBER: 'number',
    XL_CELL_DATE: 'xldate',
    XL_CELL_BOOLEAN: 'bool',
    XL_CELL_ERROR: 'error',
    XL_CELL_BLANK: 'blank'
}