'''

Unit-test runner that runs all unit-tests in the project.

Copyright (C) 2015    Andrei Novikov (spb.andr@yandex.ru)

pyclustering is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyclustering is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

import unittest;

from pyclustering.clustering.birch               import tests as cluster_birch_unit_tests;
from pyclustering.clustering.cure                import tests as cluster_cure_unit_tests;
from pyclustering.clustering.dbscan              import tests as cluster_dbscan_unit_tests;
from pyclustering.clustering.hierarchical        import tests as cluster_hierarchical_unit_tests;
from pyclustering.clustering.hsyncnet            import tests as cluster_hsyncnet_unit_tests;
from pyclustering.clustering.kmeans              import tests as cluster_kmeans_unit_tests;
from pyclustering.clustering.optics              import tests as cluster_optics_unit_tests;
from pyclustering.clustering.rock                import tests as cluster_rock_unit_tests;
from pyclustering.clustering.syncnet             import tests as cluster_syncnet_unit_tests;
from pyclustering.clustering.syncsom             import tests as cluster_syncsom_unit_tests;
from pyclustering.clustering.xmeans              import tests as cluster_xmeans_unit_tests;

from pyclustering.gcolor.dsatur                  import tests as gcolor_dsatur_unit_tests;
from pyclustering.gcolor.hysteresis              import tests as gcolor_hysteresis_unit_tests;
from pyclustering.gcolor.sync                    import tests as gcolor_sync_unit_tests;

from pyclustering.nnet.hhn                       import tests as nnet_hhn_unit_tests;
from pyclustering.nnet.hysteresis                import tests as nnet_hysteresis_unit_tests;
from pyclustering.nnet.legion                    import tests as nnet_legion_unit_tests;
from pyclustering.nnet.pcnn                      import tests as nnet_pcnn_unit_tests;
from pyclustering.nnet.som                       import tests as nnet_som_unit_tests;
from pyclustering.nnet.sync                      import tests as nnet_sync_unit_tests;
from pyclustering.nnet                           import tests as nnet_unit_tests;

from pyclustering.support.cftree                 import tests as support_cftree_unit_tests;
from pyclustering.support.kdtree                 import tests as support_kdtree_unit_tests;
from pyclustering.support                        import tests as support_unit_tests;



if __name__ == "__main__":
    suite = unittest.TestSuite();
    
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cluster_birch_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cluster_cure_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cluster_dbscan_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cluster_hierarchical_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cluster_hsyncnet_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cluster_kmeans_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cluster_optics_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cluster_rock_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cluster_syncnet_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cluster_syncsom_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cluster_xmeans_unit_tests));
     
    suite.addTests(unittest.TestLoader().loadTestsFromModule(gcolor_dsatur_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(gcolor_hysteresis_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(gcolor_sync_unit_tests));
 
    suite.addTests(unittest.TestLoader().loadTestsFromModule(nnet_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(nnet_hhn_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(nnet_hysteresis_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(nnet_legion_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(nnet_pcnn_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(nnet_som_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(nnet_sync_unit_tests));
    
    suite.addTests(unittest.TestLoader().loadTestsFromModule(support_cftree_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(support_kdtree_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(support_unit_tests));
    
    unittest.TextTestRunner(verbosity = 2).run(suite);
    