from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Basic theme which only uses colors in 0-15 range"""
    USERNAME_FG = 232
    USERNAME_BG = 201
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 8
    HOSTNAME_BG = 7

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 236
    PATH_FG = 207
    CWD_FG = 213
    SEPARATOR_FG = 27

    READONLY_BG = 1
    READONLY_FG = 15

    REPO_CLEAN_BG = 2   # green
    REPO_CLEAN_FG = 0   # black
    REPO_DIRTY_BG = 1   # red
    REPO_DIRTY_FG = 15  # white

    JOBS_FG = 197
    JOBS_BG = 237

    CMD_PASSED_BG = 238
    CMD_PASSED_FG = 219
    CMD_FAILED_BG = 11
    CMD_FAILED_FG = 0

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0

    AWS_PROFILE_FG = 14
    AWS_PROFILE_BG = 8

    TIME_FG = 8
    TIME_BG = 7
