import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("kubernetes_masters")


def test_helm_command(host):
    assert host.find_command("helm")


def test_helm_installed_plugins(host):
    result = host.run("helm plugin list")
    assert result.rc == 0
    plugins = [line.split()[0] for line in result.stdout.split("\n")[1:-1]]
    assert "diff" in plugins
