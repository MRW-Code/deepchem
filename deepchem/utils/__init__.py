"""
Miscellaneous utility functions.
"""
# flake8: noqa
import logging

logger = logging.getLogger(__name__)

from deepchem.utils.misc_utils import indent
from deepchem.utils.misc_utils import shape2str

from deepchem.utils.batch_utils import batch_coulomb_matrix_features

from deepchem.utils.attribute_utils import set_attr
from deepchem.utils.attribute_utils import get_attr
from deepchem.utils.attribute_utils import del_attr

from deepchem.utils.conformers import ConformerGenerator
from deepchem.utils.evaluate import relative_difference
from deepchem.utils.evaluate import Evaluator
from deepchem.utils.evaluate import GeneratorEvaluator

from deepchem.utils.coordinate_box_utils import CoordinateBox
from deepchem.utils.coordinate_box_utils import intersect_interval
from deepchem.utils.coordinate_box_utils import intersection
from deepchem.utils.coordinate_box_utils import union
from deepchem.utils.coordinate_box_utils import merge_overlapping_boxes
from deepchem.utils.coordinate_box_utils import get_face_boxes

from deepchem.utils.data_utils import pad_array
from deepchem.utils.data_utils import get_data_dir
from deepchem.utils.data_utils import download_url
from deepchem.utils.data_utils import untargz_file
from deepchem.utils.data_utils import unzip_file
from deepchem.utils.data_utils import UniversalNamedTemporaryFile
from deepchem.utils.data_utils import load_image_files
from deepchem.utils.data_utils import load_sdf_files
from deepchem.utils.data_utils import load_csv_files
from deepchem.utils.data_utils import load_json_files
from deepchem.utils.data_utils import load_pickle_files
from deepchem.utils.data_utils import load_data
from deepchem.utils.data_utils import save_to_disk
from deepchem.utils.data_utils import load_from_disk
from deepchem.utils.data_utils import save_dataset_to_disk
from deepchem.utils.data_utils import load_dataset_from_disk
from deepchem.utils.data_utils import remove_missing_entries

from deepchem.utils.debug_utils import get_print_threshold
from deepchem.utils.debug_utils import set_print_threshold
from deepchem.utils.debug_utils import get_max_print_size
from deepchem.utils.debug_utils import set_max_print_size

from deepchem.utils.fragment_utils import AtomShim
from deepchem.utils.fragment_utils import MolecularFragment
from deepchem.utils.fragment_utils import get_partial_charge
from deepchem.utils.fragment_utils import merge_molecular_fragments
from deepchem.utils.fragment_utils import get_mol_subset
from deepchem.utils.fragment_utils import strip_hydrogens
from deepchem.utils.fragment_utils import get_contact_atom_indices
from deepchem.utils.fragment_utils import reduce_molecular_complex_to_contacts

from deepchem.utils.genomics_utils import seq_one_hot_encode
from deepchem.utils.genomics_utils import encode_bio_sequence

from deepchem.utils.geometry_utils import unit_vector
from deepchem.utils.geometry_utils import angle_between
from deepchem.utils.geometry_utils import generate_random_unit_vector
from deepchem.utils.geometry_utils import generate_random_rotation_matrix
from deepchem.utils.geometry_utils import is_angle_within_cutoff
from deepchem.utils.geometry_utils import compute_centroid
from deepchem.utils.geometry_utils import subtract_centroid
from deepchem.utils.geometry_utils import compute_protein_range
from deepchem.utils.geometry_utils import compute_pairwise_distances

from deepchem.utils.graph_utils import fourier_encode_dist
from deepchem.utils.graph_utils import aggregate_mean
from deepchem.utils.graph_utils import aggregate_max
from deepchem.utils.graph_utils import aggregate_min
from deepchem.utils.graph_utils import aggregate_std
from deepchem.utils.graph_utils import aggregate_var
from deepchem.utils.graph_utils import aggregate_moment
from deepchem.utils.graph_utils import aggregate_sum
from deepchem.utils.graph_utils import scale_identity
from deepchem.utils.graph_utils import scale_amplification
from deepchem.utils.graph_utils import scale_attenuation

from deepchem.utils.hash_utils import hash_ecfp
from deepchem.utils.hash_utils import hash_ecfp_pair
from deepchem.utils.hash_utils import vectorize

from deepchem.utils.molecule_feature_utils import one_hot_encode
from deepchem.utils.molecule_feature_utils import get_atom_type_one_hot
from deepchem.utils.molecule_feature_utils import construct_hydrogen_bonding_info
from deepchem.utils.molecule_feature_utils import get_atom_hydrogen_bonding_one_hot
from deepchem.utils.molecule_feature_utils import get_atom_is_in_aromatic_one_hot
from deepchem.utils.molecule_feature_utils import get_atom_hybridization_one_hot
from deepchem.utils.molecule_feature_utils import get_atom_total_num_Hs_one_hot
from deepchem.utils.molecule_feature_utils import get_atom_chirality_one_hot
from deepchem.utils.molecule_feature_utils import get_atom_formal_charge
from deepchem.utils.molecule_feature_utils import get_atom_formal_charge_one_hot
from deepchem.utils.molecule_feature_utils import get_atom_partial_charge
from deepchem.utils.molecule_feature_utils import get_atom_total_degree_one_hot
from deepchem.utils.molecule_feature_utils import get_bond_type_one_hot
from deepchem.utils.molecule_feature_utils import get_bond_is_in_same_ring_one_hot
from deepchem.utils.molecule_feature_utils import get_bond_is_conjugated_one_hot
from deepchem.utils.molecule_feature_utils import get_bond_stereo_one_hot
from deepchem.utils.molecule_feature_utils import get_bond_graph_distance_one_hot

from deepchem.utils.pdbqt_utils import pdbqt_to_pdb
from deepchem.utils.pdbqt_utils import convert_protein_to_pdbqt
from deepchem.utils.pdbqt_utils import convert_mol_to_pdbqt

from deepchem.utils.docking_utils import write_vina_conf
from deepchem.utils.docking_utils import write_gnina_conf
from deepchem.utils.docking_utils import read_gnina_log
from deepchem.utils.docking_utils import load_docked_ligands
from deepchem.utils.docking_utils import prepare_inputs

from deepchem.utils.voxel_utils import convert_atom_to_voxel
from deepchem.utils.voxel_utils import convert_atom_pair_to_voxel
from deepchem.utils.voxel_utils import voxelize

from deepchem.utils.sequence_utils import hhblits
from deepchem.utils.sequence_utils import hhsearch

try:
    from deepchem.utils.periodic_table_utils import get_atomz
    from deepchem.utils.periodic_table_utils import get_atom_mass
    from deepchem.utils.periodic_table_utils import get_period

    from deepchem.utils.pytorch_utils import unsorted_segment_sum
    from deepchem.utils.pytorch_utils import segment_sum
    from deepchem.utils.pytorch_utils import chunkify
    from deepchem.utils.pytorch_utils import get_memory

    from deepchem.utils.safeops_utils import safepow
    from deepchem.utils.safeops_utils import safenorm
    from deepchem.utils.safeops_utils import occnumber
    from deepchem.utils.safeops_utils import get_floor_and_ceil
    from deepchem.utils.safeops_utils import safe_cdist
except ModuleNotFoundError as e:
    logger.warning(
        f'Skipped loading some Pytorch utilities, missing a dependency. {e}')
