import sys
from subprocess import call

FAIL_UNDER = "90"
COV = ["coverage"]
RUN = ["run", "--source=tox", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = [
    "allowed_implicit_cli_envs",
    "build_wheel_in_non_base_pkg_env",
    "constrain_package_deps",
    "dependency_groups_include",
    "dependency_groups_multiple",
    "dependency_groups_single",
    "deps_remove_recreate",
    "env_log",
    "find_alias_on_path",
    "get_info_uses_hook_path",
    "ini_exhaustive_parallel_values",
    "install_command_no_packages",
    "install_pkg_via",
    "keyboard_interrupt",
    "legacy_cli_flags",
    "local_subprocess",
    "override_incorrect",
    "package_only",
    "package_pyproject",
    "parallel_inception",
    "parallel_interrupt",
    "pip_install_constraint_file_create_change",
    "pip_install_constraint_file_new",
    "pip_install_path",
    "pip_install_req_file_req_like",
    "pip_install_requirements_file_deps",
    "pip_pre",
    "pip_req_path",
    "pkg_dep_remove_recreate",
    "pkg_env_dep_remove_recreate",
    "plugin_hooks_and_order",
    "provision_interrupt_child",
    "provision_non_canonical_dep",
    "pyproject_deps_from_static",
    "pyproject_deps_static_with_dynamic",
    "pyproject_no_build_editable_fallback",
    "python_disable_hash_seed",
    "python_generate_hash_seed",
    "python_hash_seed_from_env_and_disable",
    "python_hash_seed_from_env_and_override",
    "python_keep_hash_seed",
    "python_set_hash_seed",
    "requirements_txt",
    "skip_develop_mode",
    "some_files_exist",
    "tox_install_pkg_sdist",
    "tox_install_pkg_wheel",
    "verbosity_guess_miss_match",
]
SKIP_OR = " or ".join(SKIPS)
K = ["-k", f"not ({SKIP_OR})"]


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST, *K])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
