# -*- coding: utf-8 -*-
# Name:         __init__.py
# Author:       小菜
# Date:         2023/4/28 11:23
# Description:

import os
import sys

from .config_utils import read_ini_config
from .date_utils import (
    get_date_range,
    date_diff_days,
    date_str_to_date
)
from .excel_utils import dict_to_excel
from .html_utils import (
    html_to_dom,
    extract_title,
    extract_links,
    parse_xpath
)
from .json_utils import (
    read_json,
    write_json,
    add_to_json,
    update_json,
    delete_from_json
)
from .network_utils import (
    build_url,
    send_request
)
from .os_utils import (
    check_file_exists,
    normalize_file_path,
    join_file_path
)
from .string_utils import replace_string
from .window_utils import (
    minimize_window,
    maximize_window,
    set_top_window,
    close_window,
    hide_window,
    show_window
)
