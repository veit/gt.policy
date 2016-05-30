# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from gt.policy.testing import GT_POLICY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that gt.policy is properly installed."""

    layer = GT_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if gt.policy is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'gt.policy'))

    def test_browserlayer(self):
        """Test that IGtPolicyLayer is registered."""
        from gt.policy.interfaces import (
            IGtPolicyLayer)
        from plone.browserlayer import utils
        self.assertIn(IGtPolicyLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = GT_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['gt.policy'])

    def test_product_uninstalled(self):
        """Test if gt.policy is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'gt.policy'))

    def test_browserlayer_removed(self):
        """Test that IGtPolicyLayer is removed."""
        from gt.policy.interfaces import IGtPolicyLayer
        from plone.browserlayer import utils
        self.assertNotIn(IGtPolicyLayer, utils.registered_layers())
